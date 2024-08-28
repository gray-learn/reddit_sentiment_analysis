import csv
import pandas as pd
from langchain_community.document_loaders import UnstructuredPDFLoader

local_path = "data/r66_mm_12.pdf"

# Local PDF file uploads
if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
else:
    print("Upload a PDF file")

# Preview first page
print('First page content:')

# print(data)
# print(data[0].page_content)

# Export page content to Excel
output_path = "data/output.xlsx"

# Create a DataFrame
df = pd.DataFrame({"Page Content": [data[0].page_content for page in data]})

# Save DataFrame to Excel
df.to_excel(output_path, index=False)
