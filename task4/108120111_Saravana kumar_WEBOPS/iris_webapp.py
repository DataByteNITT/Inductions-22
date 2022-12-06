import streamlit as st
import pickle



lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))

def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Virginica'
def main():
    html = """
    <div style="background-color:skyblue;padding:10px">
    <h2 style="color:gray;text-transform:uppercase;text-shadow:3px 1px 2px red;text-align:center;">Iris Classification</h2>
    <h3 style="color:orange;text-shadow:1px 2px 3px blue;">There are Three Classification,They are Setosa,Virginia,Veronica.
    According to the datasetvalues,the classified result will change and displayed below.</h3></div>
    """

    st.markdown(html, unsafe_allow_html=True)
    activities=['Linear Regression','Logistic Regression']
    option=st.sidebar.selectbox('choose any model',activities)
    st.subheader(option)
    sl=st.number_input('Select Sepal Length', 0.0, 10.0)
    sw=st.number_input('Select Sepal Width', 0.0, 10.0)
    pl=st.number_input('Select Petal Length', 0.0, 10.0)
    pw=st.number_input('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Linear Regression':
            st.success(classify(lin_model.predict(inputs)))
    
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))

if __name__=='__main__':
    main()