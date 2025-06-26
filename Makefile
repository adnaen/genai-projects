DOC_SEARCHER=search_with_documents

run:
ifeq ($(name), 1)
	uvicorn $(DOC_SEARCHER).main:app --reload
else
	echo "avilable options: [1], got $(name)"
endif

