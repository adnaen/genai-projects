import { useState } from "react";
import { Button } from "../ui/button";
import { Input } from "../ui/input";

const ResumeUploadForm = () => {
	const [file, setFile] = useState<any | null>(null)
	const [isDisabled, setIsDiabled] = useState<boolean>(true);

	return (
		<form className="flex flex-col gap-3 max-w-3/5 w-2/5 items-center">
			<h1 className="text-2xl font-extralight">Upload your Resume</h1>
			<div className="text-center">
				<Input type="file" className="" onChange={(e) => { setFile(e.target.value); setIsDiabled(!isDisabled) }} />
				<p className="text-sm text-slate-300">supported files: <span className="text-white">(pdf, docx)</span></p>
			</div>

			<Button disabled={isDisabled} variant={"secondary"} className="w-2/3">Analyze</Button>

			{file !== null && (
				<span> {file}</span>
			)}
		</form >
	)
}

export default ResumeUploadForm;
