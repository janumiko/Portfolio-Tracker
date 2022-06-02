FROM python:3.10

WORKDIR /portfolio_tracker

# copy everything to the container
COPY . .

# install dependencies of the app
RUN pip install -r requirements.txt

# expose port 8501 used by streamlit
EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["portfolio_tracker.py"]
