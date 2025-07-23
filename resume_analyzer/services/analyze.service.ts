export class AnalyzeResumeService {
  static readonly NEXT_PUBLIC_API_URL = process.env.NEXT_PUBLIC_API_URL;

  static async analyzeResume(file: File): Promise<string> {
    const formData = new FormData()
    formData.append('file', file)
    try {
      const response = await fetch(`${this.NEXT_PUBLIC_API_URL}/analyze`, {
        method: "POST",
        body: formData,
      })
      const data = await response.json()
      return data.assistant
    } catch (err) {
      return ""
    }
  }
}
