from flask import Flask, render_template
app = Flask(__name__)

dummy_data = [
    {
        "authour": "Nosa Agho",
        "title": "First Blog Post Title",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo, impedit.",
        "date_posted": "October, 13, 2021",
    },
    {
        "authour": "John Doe",
        "title": "Second Blog Post Title",
        "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolores recusandae aliquam exercitationem, accusamus odio corrupti saepe provident dolor id officia?",
        "date_posted": "October, 14, 2021",
    }
]


@app.route("/")
def hello():
    return render_template('home.html', posts=dummy_data)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
