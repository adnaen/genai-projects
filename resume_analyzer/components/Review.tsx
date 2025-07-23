const ResumeReview = ({ assistantResponse }: { assistantResponse: string }) => {
	return (
		<div className="my-10">
			<h1 className="text-3xl font-bold">Insightes</h1>
			<span>{assistantResponse}</span>
		</div>
	)
}

export default ResumeReview;
