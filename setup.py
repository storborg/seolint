from setuptools import setup


setup(name="seolint",
      version='0.1',
      description="SEO linting tool.",
      long_description='',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='seo keywords crawl search tags ranking',
      author='Scott Torborg',
      author_email='storborg@mit.edu',
      url='http://github.com/storborg/seolint',
      install_requires=[
          'lxml',
      ],
      license='MIT',
      packages=['seolint'],
      entry_points=dict(console_scripts=['seolint=seolint:main']),
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
