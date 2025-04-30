import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    # Welcome to the Enverge
    return


@app.cell
def _():
    ## This is a demo of a conversion to Marimo
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # prompt: generate a sample pandas dataframe with fruits

    data = {'Fruits': ['Apple', 'Banana', 'Orange', 'Grape']}
    df = pd.DataFrame(data)

    df
    return


if __name__ == "__main__":
    app.run()
