export class AnalyzeResume {
  static readonly NEXT_PUBLIC_API_URL = process.env.NEXT_PUBLIC_API_URL;

  static async analyzeResume(file: File): Promise<string[]> {
    const formData = new FormData()
    formData.append('file', file)
    try {
      const response = await fetch(`${this.NEXT_PUBLIC_API_URL}/analyze`, {
        method: "POST",
        body: formData,
      })
      const data: string[] = await response.json()
      return data
    } catch (err) {
      return []
    }
  }
}
