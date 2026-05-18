from pypdf import PdfReader

def extract_pdf_text(file_path: str):

    try:

        reader = PdfReader(file_path)

        page_count=len(reader.pages)

        text=[]

        for page in reader.pages:

            content=page.extract_text()

            if content:
                text.append(content)

        final_text="\n".join(text)

        return{

            "success":True,
            "pages":page_count,
            "characters":len(final_text),
            "text":final_text

        }

    except Exception as e:

        return{

            "success":False,
            "error":str(e)

        }