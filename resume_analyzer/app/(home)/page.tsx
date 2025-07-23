"use client"
import ResumeUploadForm from "@/components/forms/ResumeUploadForm";
import ResumeReview from "@/components/Review";
import { AnalyzeResumeService } from "@/services/analyze.service";
import { useState } from "react";

export default function Home() {
  const [assistantResponse, setAssistantResponse] = useState<string>("")

  const onSubmit = async (file: File) => {
    const response = await AnalyzeResumeService.analyzeResume(file)
    setAssistantResponse(response)
    console.log(response)
  }
  return (
    <div className="flex justify-center h-sreen flex-col">
      <h1 className="text-5xl font-bold text-center my-10">Resume Analyzer</h1>
      <div className="h-auto flex justify-center">
        <ResumeUploadForm onSubmit={onSubmit} />
      </div>
      <div className="p-5">
        <ResumeReview assistantResponse={assistantResponse} />
      </div>
    </div>
  );
}
