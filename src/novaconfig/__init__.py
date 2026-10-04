import os
import typer
app=typer.Typer(no_args_is_help=True)
@app.command()
def check(required: str=typer.Option(...,"--required",help="Comma-separated variable names"))->None:
    missing=[name.strip() for name in required.split(",") if name.strip() and not os.environ.get(name.strip())]
    if missing: typer.echo("Missing required variables: "+", ".join(missing),err=True); raise typer.Exit(1)
    typer.echo("Configuration requirements satisfied.")
