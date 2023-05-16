from flask import Flask, jsonify, request

app = Flask(__name__)
all_article = []

@app.route("/get-recommendations",encoding="utf-8")
def get_article():
    article_data = {
        "title": all_article[0][19],
        "poster_link": all_article[0][27],
        "release_date": all_article[0][13] or "N/A",
        "duration": all_article[0][15],
        "rating": all_article[0][20],
        "overview": all_article[0][9]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"],encoding="utf-8")
def liked_article():
    liked_articles = []
    article = all_article[0]
    liked_articles.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 200

@app.route("/unliked-article" ,methods=["POST"],encoding="utf-8")
def unliked_article():
    not_liked_articles = []
    article = all_article[0]
    not_liked_articles.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch-article" ,methods=["POST"],encoding="utf-8")
def did_not_watch_view():
    did_not_watch_article = []
    article = all_article[0]
    did_not_watch_article.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 200
    
@app.route("/article-movies",encoding = 'utf-8')
def popular_movies():
    article_data = []
    for movie in output:
        _d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-movies",encoding = 'utf-8')
def recommended_movies():
    all_recommended = []
    for liked_articles in liked_article:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()