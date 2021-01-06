import json
import flask
import fetch

app = flask.Flask(__name__)


@app.route("/")
def index():
    cats, langs = fetch.all_languages(sortBy="cat")
    count = len(fetch.all_languages(sortBy="abc"))

    return flask.render_template("index.html", langs=langs, cats=cats, c=count)


@app.route("/<name>")
def language(name: str):
    lang = None
    langs = fetch.all_languages(sortBy="abc")
    valids = ["name", "category", "displayName", "image", "tagline", "entrypoint"]

    for l in langs:
        if l["name"] == name:
            lang = l
        else:
            pass

    if not lang:
        return flask.abort(404)
    else:
        try:
            cmd = " ".join(lang["run"]["command"])
        except KeyError:
            cmd = None

        try:
            is_temp = bool(lang["template"])
        except KeyError:
            is_temp = False

        icon = fetch.format_icon(lang["icon"])
        raw = json.dumps(lang, indent=2)

        return flask.render_template(
            "lang.html",
            lang=lang,
            cmd=cmd,
            icon=icon,
            is_temp=is_temp,
            valids=valids,
            raw=raw,
        )

app.run(host="0.0.0.0", port=8080, threaded=True)
