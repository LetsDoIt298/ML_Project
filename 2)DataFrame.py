import streamlit as st  
import pandas as pd

def df_read(file_name):
    '''This function will be used to read a file(csv/exel)'''
    ext=''
    for i in file_name[::-1]:
        if i=='.':
            ext = ext[::-1]
            break
        ext = ext+i
    if ext=='xlsx':
        print("NNNNNNNNNNNNNNNN")
        df = pd.read_excel(file_name)
        return df
    if ext=='csv':
        df = pd.read_csv(file_name)
        return df

def DataFrame(df):
    # # Create two columns
    # button_column1, button_column2 = st.columns(2)
    
    # # Button 1
    # if button_column1.button("Button 1"):
    #     st.write("Button 1 clicked!")

    # # Button 2
    # if button_column2.button("Button 2"):
    #     st.write("Button 2 clicked!")


    # if st.button("Toggle Display DataFrame"):
    #     # Toggle the visibility of the DataFrame
    #     if 'show_df' not in st.session_state:
    #         st.session_state.show_df = True
    #     else:
    #         st.session_state.show_df = not st.session_state.show_df
    
    button_column1, button_column2 ,button_column3,button_column4= st.columns(4)
    if button_column1.button("View Data"):
        st.dataframe(df.head())
    if button_column2.button("Data Size"):
        st.text(f'Number of rows:-{df.shape[0]} \nNumber of columns:-{df.shape[1]}')
    if button_column3.button("Audience Finder"):
        auf(df)
        
    
def auf(df):
    # Display the list in a box with a scroll bar
    st.sidebar.text("List:")
    st.sidebar.text("\n".join(list(df.columns)))
    market = st.text_input("Choose the market")
    submit1 = st.button("Submit")
    
    if submit1==True:
        print('HI')
        st.write("Enter the Market is",market)


def main():
    st.title("File Uploader Example")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

    if uploaded_file is not None:
        # Process the uploaded file
        st.write("File Uploaded Successfully!")
        #st.write("File Name:", uploaded_file.name)
        #st.write("File Type:", uploaded_file.type)
        #st.write("File Size (bytes):", uploaded_file.size)
        # You can further process the content of the file if needed
        # Example: df = pd.read_csv(uploaded_file)
        df = df_read(uploaded_file.name)
        DataFrame(df)
if __name__ == "__main__":
    main()