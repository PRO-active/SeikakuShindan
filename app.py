import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 仮想的な性格診断データ
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    '内向性・外向性': [4, 2, 5, 1, 3],
    '論理型・感覚型': [3, 4, 2, 5, 1],
    '計画型・柔軟型': [5, 3, 1, 4, 2],
    '五感型・直感型': [2, 5, 3, 1, 4]
}

ratings = pd.DataFrame(data).set_index('User')

def recommend_personality(user_ratings, target_user):
    user_similarity = cosine_similarity(user_ratings)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_ratings.index, columns=user_ratings.index)

    similar_users = user_similarity_df[target_user].sort_values(ascending=False)[1:]

    most_similar_user = similar_users.index[0]
    return most_similar_user

st.title('性格マッチングシステム')

st.write('いくつかの質問に答えてください。それに基づいてあなたに似た性格を持つ人とマッチングします。')

intro_extro = st.slider('あなたの内向性・外向性（1:内向的 〜 5:外向的）', 1, 5, 3)
thinking_feeling = st.slider('あなたの論理型・感覚型（1:論理型 〜 5:感覚型）', 1, 5, 3)
judging_perceiving = st.slider('あなたの計画型・柔軟型（1:計画型 〜 5:柔軟型）', 1, 5, 3)
sensing_intuition = st.slider('あなたの五感型・直感型（1:五感型 〜 5:直感型）', 1, 5, 3)

new_user_ratings = pd.Series({
    '内向性・外向性': intro_extro,
    '論理型・感覚型': thinking_feeling,
    '計画型・柔軟型': judging_perceiving,
    '五感型・直感型': sensing_intuition
})

ratings.loc['NewUser'] = new_user_ratings

similar_user = recommend_personality(ratings, 'NewUser')
if st.button("結果を見る"):
    st.write(f'あなたに最も似た性格タイプのユーザーは: {similar_user} です！')

    st.write('このユーザーの性格診断結果：')
    st.write(ratings.loc[similar_user])