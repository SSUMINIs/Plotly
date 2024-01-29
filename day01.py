import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def main():
    #graph_objects
    fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
            layout=go.Layout(title=go.layout.Title(text="A Figure Specified By A Graph Object")
        )
    )
    st.plotly_chart(fig)

    #express
    import plotly.express as px

    # px.bar() 함수를 활용해서 bar chart 생성과 동시에 Data, Layout 값 입력
    fig = px.bar(x=[1, 2, 3], y=[1, 3, 2],title="A Figure Specified By express")
    st.plotly_chart(fig)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
    st.plotly_chart(fig)


    fig = make_subplots(rows=1, cols=2)
    fig.add_bar(y=[1, 2, 3],
            marker=dict(color="red"),
            name="b", row=1, col=1)
    fig.add_scatter(y=[1, 3, 2], mode="markers",
                marker=dict(size=20, color="red"),
                name="c", row=1, col=2)
    fig.update_traces(marker=dict(color="blue"),
                  selector=dict(type="bar"))
    st.plotly_chart(fig)

    fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
    fig.update_layout(title_text="update_layout 사용",title_font_size=30)
    st.plotly_chart(fig)
   
    #축설정
    df = px.data.tips()
    fig = go.Figure(data=go.Scatter(x=df["total_bill"], y=df["tip"], mode='markers'))
    fig.update_xaxes(title_text='Total Bill ($)')
    fig.update_yaxes(title_text='Tip ($)')
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
