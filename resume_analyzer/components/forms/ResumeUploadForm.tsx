import { useState } from "react";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { Loader } from "lucide-react";

const ResumeUploadForm = ({ onSubmit }: { onSubmit: (file: File) => void }) => {
	const [file, setFile] = useState<File | null>(null)
	const [roleDescription, setRoleDescription] = useState<string>("");
	const [isDisabled, setIsDiabled] = useState<boolean>(true);
	const [isGenerating, setIsGenerating] = useState<boolean>(false);

	const handleFormSubmission = async (e: React.FormEvent) => {
		e.preventDefault()
		if (file !== null) {
			console.log("its called hehe")
			setIsGenerating(true);
			setIsDiabled(true);
			await onSubmit(file)
			setIsDiabled(false);
			setIsGenerating(false);
		}
	}

	const handleFileInputOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setIsDiabled(!isDisabled)
		if (e.target.files && e.target.files.length > 0) {
			setFile(e.target.files[0])
		}
	}

	return (
		<form className="flex flex-col gap-3 max-w-3/5 w-2/5 items-start" onSubmit={handleFormSubmission}>
			<h1 className="text-2xl font-extralight">Upload your Resume</h1>
			<div className="text-center w-full">
				<Input type="file" className="" onChange={handleFileInputOnChange} />
				<p className="text-sm text-slate-300">supported files: <span className="text-white">(pdf, docx)</span></p>
			</div>

			<div className="w-full">
				<Label htmlFor="description">(optional)</Label>
				<Input placeholder="Describe about your role..." type="text" id="description" value={roleDescription} onChange={(e) => { setRoleDescription(e.target.value) }} />
			</div>

			<Button disabled={isDisabled} variant={"secondary"} className="w-full">
				{isGenerating ? (
					<span className="flex gap-3 items-center animate-pulse">Analyzing...
						<Loader className="animate-spin" />
					</span>
				) : (
					<span>Analyze</span>
				)}

			</Button>

		</form >
	)
}
export default ResumeUploadForm;
