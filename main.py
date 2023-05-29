import justpy as jp
# INSERT THIS CODE FOR RUN WITH UVICORN
app = jp.app

def Myapp():
    mapp = jp.QuasarPage()
    # a is you parent component

    mydiv = jp.Div(classes="row q-pa-md",a=mapp)
    btn = jp.QBtn(color="primary",icon="send",label="my button",a=mydiv)

    return mapp

# AND ADD THIS ARGUMENT
jp.justpy(Myapp,start_server=False)
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000,log_level="info")

