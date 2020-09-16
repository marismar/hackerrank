def designerPdfViewer(h, word):
  length = len(word)
  height = 0
  for char in word:
    if h[ord(char) - 97] > height:
      height = h[ord(char) - 97]
  return length * height