import streamlit as st


st.set_page_config(page_title="Personal Expense Tracker" ,page_icon="💰")

if "expense" not in st.session_state:
    st.session_state.expense = []
    # print("expense")
expense=st.session_state.expense
st.header("Wellcome 💰Personal Expense Tracker")

tab1,tab2,tab3 = st.tabs(["Dashboard","Add expense","Expense Recode"])


with tab1:
    
    st.subheader("Dashboard Summary")
    def total_expense():
        total_expense = 0
        
        for i in expense:
            total_expense += i["Amount"]
        return total_expense
    def total_trasection():
        total_trasection = len(expense)
        return total_trasection
    
    def heigst_expense():
        high_expense = 0
        
        for i in expense:
            if high_expense < i["Amount"]:
                high_expense = i["Amount"]
        return high_expense
    if len(expense) > 0:
        st.metric("Total Expense", total_expense())
        st.metric("Total Trasection", total_trasection())
        st.metric("Heigst Expense", heigst_expense())
    else:
        st.warning( "No Expense Found")
        st.warning( "No Trasection Found")
        st.warning( "No Heigst Expance Found")       

with tab2:
    

    st.subheader("Add expense")
    with st.form(key="expense_form" ,clear_on_submit=True):
        expense_name=st.text_input("Enter An expense Name" ,key="expense name", placeholder="expense Name")

        amount=st.number_input("Enter An expense Amount", key="expense amount", placeholder="expense Amount" , step=1)

        category=st.selectbox("Catgory", ["Food", "Shopping", "Travel", "Bills", "Others"], placeholder="Select An expense Category")

        date=st.date_input("Select Date")

        submit_button= st.form_submit_button("Add expense" ,type="primary" , use_container_width = True)

        if submit_button:
            if expense_name.strip().capitalize() == "":
                st.error("Please fill all the Fields: ")
            elif amount <= 0:
                st.error("Amount must br grater than 0")
            else:
                new_expense = {
                    "Expense Name": expense_name,
                    "Amount": amount,
                    "Category": category,
                    "Date": date
                    }
                expense.append(new_expense)
                st.success(f"Successfully added '{expense_name}' under '{category}'!")
                
                print(expense)
                st.rerun()
                
                
with tab3:
    st.subheader("Expense Recodee")
    if len(expense) > 0:
        
       st.dataframe(expense, use_container_width=True)
                        
    else:
        st.warning("No Expense Found")
        
        
        

                

                
            
            


      



