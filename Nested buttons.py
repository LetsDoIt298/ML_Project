import streamlit as st

def main():
    st.title("Three Levels of Nested Buttons Example")

    # Outer columns
    outer_column1, outer_column2 = st.columns(2)

    # Outer buttons
    if outer_column1.button("Outer Button 1"):
        st.write("Outer Button 1 clicked!")

        # First level of nested buttons within the first outer button
        if outer_column1.button("Nested Button 1.1"):
            st.write("Nested Button 1.1 clicked!")

            # Second level of nested buttons within the first nested button
            if outer_column1.button("Double Nested Button 1.1.1"):
                st.write("Double Nested Button 1.1.1 clicked!")

        if outer_column1.button("Nested Button 1.2"):
            st.write("Nested Button 1.2 clicked!")

    if outer_column2.button("Outer Button 2"):
        st.write("Outer Button 2 clicked!")

        # First level of nested buttons within the second outer button
        if outer_column2.button("Nested Button 2.1"):
            st.write("Nested Button 2.1 clicked!")

            # Second level of nested buttons within the second nested button
            if outer_column2.button("Double Nested Button 2.1.1"):
                st.write("Double Nested Button 2.1.1 clicked!")

        if outer_column2.button("Nested Button 2.2"):
            st.write("Nested Button 2.2 clicked!")

if __name__ == "__main__":
    main()
