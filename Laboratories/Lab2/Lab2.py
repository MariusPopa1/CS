import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def analyze_frequency(text):

    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    frequency = Counter(filtered_text)
    total_chars = sum(frequency.values())

    frequency_percentage = {char: (count / total_chars) * 100 for char, count in
                            frequency.items()} if total_chars > 0 else {}

    return frequency_percentage


def substitute_characters(encrypted_text, substitution_map):

    substituted_text = ''.join(substitution_map.get(char.lower(), char) for char in encrypted_text)
    return substituted_text


def main():
    st.title("Character Frequency Analysis")

    with open('cypher.txt', 'r', encoding='utf-8') as file:
        encrypted_text = file.read()

    frequency = analyze_frequency(encrypted_text)

    freq_df = pd.DataFrame(list(frequency.items()), columns=['Letter', 'Frequency (%)'])
    freq_df = freq_df.sort_values(by='Frequency (%)', ascending=False)

    english_freq = {
        'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
        'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
        'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
        'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
        'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
        'z': 0.07
    }

    english_freq_df = pd.DataFrame(list(english_freq.items()), columns=['Letter', 'Frequency (%)'])
    english_freq_df = english_freq_df.sort_values(by='Frequency (%)', ascending=False)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Frequency in Encrypted Text")
        st.dataframe(freq_df.style.set_table_attributes('style="font-size: 15px; width: 1000px;"'))

    with col2:
        st.subheader("Standard English Letter Frequency")
        st.dataframe(english_freq_df.style.set_table_attributes('style="font-size: 0px; width: 1000px;"'))

    plt.figure(figsize=(10, 5))
    plt.bar(freq_df['Letter'], freq_df['Frequency (%)'], color='skyblue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency (%)')
    plt.title('Character Frequency in Encrypted Text')
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)

    substitution_map = {
        'a': 'b', 'b': 'q', 'c': 'f', 'd': 'u', 'e': 'j',
        'f': 'y', 'g': 'n', 'h': 'c', 'i': 'r', 'j': 'g',
        'k': 'v', 'l': 'k', 'm': 'z', 'n': 'o', 'o': 'd',
        'p': 's', 'q': 'h', 'r': 'w', 's': 'l', 't': 'a',
        'u': 'p', 'v': 'e', 'w': 't', 'x': 'i', 'y': 'x',
        'z': 'm'
    }

    decrypted_text = substitute_characters(encrypted_text, substitution_map)

    st.subheader("Decrypted Text")
    st.text_area("Decrypted Text:", decrypted_text, height=300)


if __name__ == "__main__":
    main()
