import streamlit as st
import json

def load_library():
    try:
        with open("library.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        

def save_library():
    with open("library.json","w") as file:
        json.dump(library,file,indent=4)

library=load_library()


st.title("Library Manegment System")
st.write("Here You Can Manage The Library")
menu=st.sidebar.radio("select the option",["View Library","Add Book","Remove Book","Search Book","Save and Exit"])

if menu == "View Library":
    st.sidebar.title("your Library")

    if library:
        st.table(library)
    else:
        st.warning("Your Library Is Empty")    

elif menu == "Add Book":
    st.sidebar.title("Add a Book")

    title=st.text_input("add the title")
    author=st.text_input("add the author")
    year=st.number_input("add the year of release",min_value=2000,max_value=2025)
    genre=st.text_input("genre")
    read_status=st.checkbox("mark as read")

    if st.button("add book"):
        library.append({"title":title,"author":author,"year":year,"genre":genre,"read_status":read_status})
        save_library()
        st.success("Book Added Successfully")

elif menu=="Remove Book":

    st.sidebar.title("Remove Book")
    
    book_title= [book["title"] for book in library]

    if book_title:
        selected_books=st.selectbox("enter the book",book_title)

        if st.button("removed book"):
            library=[book for book in library if book["title"] != selected_books]
            save_library()
            st.success("Book Removed Successfully")
            st.rerun()
    else:
        st.warning("No Book In Library")

elif menu=="Search Book":
    search_term=st.text_input("enter the name of author or title of Book")

    if st.button("search book"):
        result=[book for book in library if search_term.lower() in book["title"].lower() or  search_term.lower() in book["author"].lower()]
        st.table(result)
    else:
        st.warning("No Book Found")

elif menu=="Save and Exit":
    save_library()
    st.success("Save Library SuccesFully")            
