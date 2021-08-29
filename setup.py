from setuptools import setup, find_packages

setup(
	name='storeql',
	version = '1.0.1',
	packages=find_packages(),
	description='Storeql is a CLI to store your passwords!',
	author='Kirai',
	author_email='allerborndaniel54@gmail.com',
	url='https://github.com/Kiraixda/storeql',
	download_url='https://github.com/Kiraixda/storeql/archive/refs/tags/1.0.1.tar.gz',
	keywords=['FAST','VAULT','CLI'],
	include_package_data=True,
	install_requirements=['click', 'colorama'],
	entry_points='''
		[console_scripts]
		storeql=storeql.__main__:cli
	'''
	)