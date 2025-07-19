import { useState } from "react";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { AnalyzeResume } from "@/services/analyze.service";

const ResumeUploadForm = () => {
	const [file, setFile] = useState<File | null>(null)
	const [isDisabled, setIsDiabled] = useState<boolean>(true);
	if (file) {
		console.log(file)
	}
	const handleFormSubmission = async (e: React.FormEvent) => {
		e.preventDefault()
		if (file !== null) {
			const response = await AnalyzeResume.analyzeResume(file)
			console.log(response)
		}
	}

	const handleFileInputOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setIsDiabled(!isDisabled)
		if (e.target.files && e.target.files.length > 0) {
			setFile(e.target.files[0])
		}
	}

	return (
		<form className="flex flex-col gap-3 max-w-3/5 w-2/5 items-center" onSubmit={handleFormSubmission}>
			<h1 className="text-2xl font-extralight">Upload your Resume</h1>
			<div className="text-center">
				<Input type="file" className="" onChange={handleFileInputOnChange} />
				<p className="text-sm text-slate-300">supported files: <span className="text-white">(pdf, docx)</span></p>
			</div>

			<Button disabled={isDisabled} variant={"secondary"} className="w-2/3">Analyze</Button>

		</form >
	)
}

export default ResumeUploadForm;
