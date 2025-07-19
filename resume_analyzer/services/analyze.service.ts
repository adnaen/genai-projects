class AnalyzeResume {
  static readonly NEXT_PUBLIC_API_URL = process.env.NEXT_PUBLIC_API_URL;

  static async analyzeResume(): Promise<string[]> {
    try {
      const response = await fetch(`${this.NEXT_PUBLIC_API_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        }
      })
    } catch (err) {
    }
    return ["hai", "hai"]
  }
}
