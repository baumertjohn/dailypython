import streamlit as st


def main():
    st.write("# Kilometers ⇄ Miles Converter")
    convert_choice = st.radio(
        "Choose the conversion direction:",
        ["Kilometers to Miles", "Miles to Kilometers"],
    )

    if convert_choice == "Kilometers to Miles":
        convert_from, convert_to = "kilometers", "miles"
    else:
        convert_from, convert_to = "miles", "kilometers"

    dist_input = st.number_input(f"Enter the distance in {convert_from}:")

    convert = st.button("Convert")

    if convert_from == "kilometers":
        converted_dist = round((dist_input * 0.6214), 2)
    else:
        converted_dist = round((dist_input * 1.609), 2)

    if convert:
        st.write(
            f":green[{dist_input} {convert_from} is equal to {converted_dist} {convert_to}.]"
        )


if __name__ == "__main__":
    main()
