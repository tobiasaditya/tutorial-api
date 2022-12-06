import fastapi
import data
app = fastapi.FastAPI()

# Query Param
@app.get("/data/query")
def get_data_query(id:str):
    result = f"Data diterima {id}" 
    print(result)
    selected_data = data.data_ambil.get(id)

    if (selected_data == None):
        raise fastapi.exceptions.HTTPException(404,"data not found")

    return selected_data

#Path Param
@app.get("/data/param/{id}")
def get_data_param(id:str):
    result = f"Data diterima {id}" 
    print(result)
    selected_data = data.data_ambil.get(id)

    if (selected_data == None):
        raise fastapi.exceptions.HTTPException(404,"data not found")
    
    return selected_data
