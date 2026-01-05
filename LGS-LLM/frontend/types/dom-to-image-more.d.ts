declare module 'dom-to-image-more' {
  interface Options {
    quality?: number
    bgcolor?: string
    width?: number
    height?: number
    style?: Record<string, string>
    filter?: (node: Node) => boolean
    imagePlaceholder?: string
    cacheBust?: boolean
    useCredentials?: boolean
  }

  interface DomToImage {
    toJpeg(node: Node, options?: Options): Promise<string>
    toPng(node: Node, options?: Options): Promise<string>
    toBlob(node: Node, options?: Options): Promise<Blob>
    toPixelData(node: Node, options?: Options): Promise<Uint8ClampedArray>
    toSvg(node: Node, options?: Options): Promise<string>
  }

  const domtoimage: DomToImage
  export default domtoimage
}
