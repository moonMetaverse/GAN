import openai
import json
import config


prompt=input()
prompt = "create a blender python script to "+prompt + " use primitive material"
openai.api_key=config.apikey


output=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user",
               "content":prompt}])

code_content = output["choices"][0]["message"]["content"]

# Extract the code snippet
print(code_content)
start_index = code_content.find("import bpy")
end_index = code_content.rfind("'''")
code_snippet = code_content[start_index:end_index] if end_index>0 else code_content[start_index:]
end_index = code_content.rfind("```")
code_snippet = code_content[start_index:end_index] if end_index>0 else code_content[start_index:]
# Save code as Python file
with open("generated.py", "w") as file:
    file.write(code_content)
print(output)

## Write the stream in glb from blender script