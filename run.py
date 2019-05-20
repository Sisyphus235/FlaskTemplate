# -*- coding: utf8 -*-

from server.core import create_app

app = create_app()


@app.cli.command()
def health():
    click.echo('Health')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
