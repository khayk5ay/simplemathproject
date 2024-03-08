#!/usr/bin/env python
import click
import hello

@click.command("calladd")
@click.option("--x", prompt= "X ", help="The first number", type=int)
@click.option("--y", prompt= "Y ", help="The second number", type=int)
def calladd(x,y):
    click.echo(hello.add(x,y))

if __name__ == "__main__":
    calladd()