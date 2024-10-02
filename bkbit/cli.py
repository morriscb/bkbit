import click
from bkbit.model_converters.sheets_converter import schema2model
from bkbit.data_translators.genome_annotation_translator import gff2jsonld
from bkbit.utils.get_ncbi_taxonomy import download_ncbi_taxonomy

@click.group()
def cli():
    """A CLI tool with multiple commands."""
    pass

# Add commands to the CLI group
cli.add_command(schema2model)
cli.add_command(gff2jsonld)
cli.add_command(download_ncbi_taxonomy)

if __name__ == '__main__':
    cli()
