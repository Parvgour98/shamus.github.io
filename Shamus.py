import streamlit as st
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers

def main():
    st.title("Find the details of your caller")
    st.subheader("Enter the correct phone number starting with country code")
    st.subheader("Our website doesn't save your data")
    mobile_number = st.text_input("Enter the Phone Number: ",type="password")
    if(st.button("Track")):
        if(len(mobile_number)==0):
            st.subheader("mobile number cannot be empty, Please enter a valid phone number.")
        else:
            ch_number = phonenumbers.parse(mobile_number,'CH')
            st.success("Country Name: {}".format(geocoder.description_for_number(ch_number,"en")))
            services_operator = phonenumbers.parse(mobile_number,'RO')
            st.success("Service Operator: {}".format(carrier.name_for_number(services_operator,"en")))
        st.subheader("Developed by Parv Gour")


if __name__ == "__main__":
    main()


