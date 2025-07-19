"use client"
import ResumeUploadForm from "@/components/forms/ResumeUploadForm";
import ResumeReview from "@/components/Review";

export default function Home() {
  return (
    <div className="flex justify-center h-sreen flex-col">
      <h1 className="text-5xl font-bold text-center my-10">Resume Analyzer</h1>
      <div className="h-auto flex justify-center">
        <ResumeUploadForm />
      </div>
      <div className="p-5">
        <ResumeReview />
      </div>
    </div>
  );

