import click
from common_language.convert_spellings import convert_spelling


@click.command()
@click.argument('input-files', nargs=-1, type=click.Path(exists=True), required=True)
@click.option("--output-file", required=False, default=None, type=str)
@click.option('--britishise', required=False, default=False, is_flag=True)
def main(input_files, output_file, britishise):
    if britishise:
        british_to_american = False
    else:
        british_to_american = True

    for input_file in input_files:
        convert_spelling(
            filepath=input_file,
            output_filepath=output_file,
            british_to_american=british_to_american
        )


if __name__ == '__main__':
    main()
