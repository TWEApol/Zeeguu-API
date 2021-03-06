import flask
import zeeguu
from flask import request
from zeeguu.model import Article
from zeeguu_api.api.utils.json_result import json_result

from .utils.route_wrappers import cross_domain, with_session
from . import api, db_session


# ---------------------------------------------------------------------------
@api.route("/article_id", methods=("GET",))
# ---------------------------------------------------------------------------
@cross_domain
@with_session
def article_id():
    """

        returns the article at that URL or creates an article and returns it

        takes url as URL argument
        NOTE: the url should be encoded with quote_plus (Pyton) and encodeURIComponent(Javascript)


    :return: article id

    """

    url = request.args.get('url', '')
    if not url:
        flask.abort(400)

    try:
        article = Article.find_or_create(db_session, url)
        return json_result(dict(article_id=article.id))
    except Exception as e:
        zeeguu.log(e)
        flask.abort(500)
