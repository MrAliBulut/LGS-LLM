# Visual Question Distribution Fix

## Problem Identified

The original algorithm was **not distributing all requested visual questions**:

### Original Issue
```python
visual_for_topic = random.randint(0, min(max_visual_for_topic, remaining_visual))
if visual_for_topic > 0:
    visual_distribution[topic] = visual_for_topic
    remaining_visual -= visual_for_topic
```

**Why it failed:**
1. `random.randint(0, x)` can return `0`
2. When it returns `0`, the topic is skipped
3. Even with remaining visual questions, topics could all get `0`
4. Result: Not all visual questions distributed

**Example from logs:**
- Request 1: `visualCount: 5` → Only distributed 4 (Friendship: 1, On The Phone: 1, Adventures: 1, Science: 1)
- Request 2: `visualCount: 5` → Only distributed 2 (On The Phone: 1, Adventures: 1)

---

## Solution Implemented

**New Algorithm: Pool-Based Distribution**

```python
if visual_count > 0 and topics_list:
    # Create a pool of topics that can accommodate visual questions
    topics_pool = []
    for topic in topics_list:
        max_visual = distribution[topic]
        # Add topic to pool for each question slot it can accommodate
        topics_pool.extend([topic] * max_visual)
    
    # Shuffle the pool for randomization
    random.shuffle(topics_pool)
    
    # Assign visual questions from the shuffled pool
    for i in range(min(visual_count, len(topics_pool))):
        topic = topics_pool[i]
        visual_distribution[topic] = visual_distribution.get(topic, 0) + 1
    
    # Log warning if we can't distribute all requested visuals
    if visual_count > len(topics_pool):
        print(f"[WARNING] Requested {visual_count} visual but only {len(topics_pool)} slots available")
```

**How it works:**
1. Create a pool with one entry per available question slot per topic
   - Topic "Friendship" with 1 question → 1 entry
   - Topic "Science" with 3 questions → 3 entries
   - Total pool size = total questions available
2. Shuffle the pool for randomness
3. Assign visual questions from the first N items in the shuffled pool
4. Guarantees: All visual questions distributed (up to available slots)

---

## Verification

### Test 1: Equal distribution (5 topics, 1 question each, 5 visual)
```
Topics pool size: 5
Visual count: 5
Result: {'Natural Forces': 1, 'Friendship': 1, 'Adventures': 1, 'Science': 1, 'On The Phone': 1}
✓ All 5 visual questions distributed
```

### Test 2: More visual than slots (2 topics, 1 question each, 5 visual)
```
Topics pool size: 2
Visual count: 5
Result: {'Science': 1, 'Friendship': 1}
[WARNING] Requested 5 visual but only 2 slots available
✓ All available slots used
```

### Test 3: Mixed slots (Friendship: 2, Science: 3, 4 visual)
```
Topics pool: [Friendship, Friendship, Science, Science, Science] (5 items)
After shuffle & assignment (4 visual):
Result: Could be any 4 from the pool, respecting limits
```

---

## Benefits

✅ **Guarantees all visual questions distributed** (or uses all available slots)  
✅ **True randomization** (shuffled pool, not per-topic)  
✅ **Respects max questions per topic** (can't exceed their question count)  
✅ **Handles edge cases** (warns if insufficient slots)  
✅ **Cleaner code** (single loop, no skipped topics)  

---

## Expected Test Results

When you run the next test with:
- Distribution: `{'Friendship': 1, 'On The Phone': 1, 'Adventures': 1, 'Science': 1, 'Natural Forces': 1}`
- Visual count: `5`

You should see:
```
[DEBUG] Visual distribution: {'Friendship': 1, 'On The Phone': 1, 'Adventures': 1, 'Science': 1, 'Natural Forces': 1}
```

All 5 topics will have 1 visual question each, guaranteeing 5 images generated.

---

## Code Changes

**File:** `generate_exam.py` (Lines 145-157)

**Before:** ~11 lines with unreliable loop  
**After:** ~14 lines with guaranteed distribution

**Backwards Compatible:** Yes - same function signature, same input/output format
