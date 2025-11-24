"""
Example Python file to demonstrate and test formatting tools.

This file contains various formatting scenarios to validate that Ruff, MyPy,
and other tools are working correctly with the GOSH team configuration.
"""

import os
from typing import Dict,List,Optional,Union
import sys
import pandas as pd
from pathlib import Path
import logging


# Example of a function that should trigger formatting
def poorly_formatted_function(x,y,z=None):
    """Example function with poor formatting that Ruff should fix."""
    if z is None:z=[]
    result=x+y
    for i in range(len(z)):
        result+=z[i]
    return result


class BioinformaticsAnalyzer:
    """Example class demonstrating Google-style docstrings and type hints."""

    def __init__(self,data_path:Union[str,Path],verbose:bool=False):
        """Initialize the analyzer.

        Args:
            data_path: Path to the input data file.
            verbose: Whether to enable verbose logging.
        """
        self.data_path=Path(data_path)
        self.verbose=verbose
        self.results:Dict[str,float]={}

    def load_data(self) -> Optional[pd.DataFrame]:
        """Load data from file.

        Returns:
            DataFrame containing the loaded data, or None if loading fails.

        Raises:
            FileNotFoundError: If the data file doesn't exist.
        """
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_path}")

        try:
            # This long line should be wrapped by the formatter to 120 characters maximum which is our team standard
            data=pd.read_csv(self.data_path,sep="\t",header=0,index_col=None,skiprows=None,nrows=None,encoding="utf-8")
            return data
        except Exception as e:logging.error(f"Failed to load data: {e}");return None

    def calculate_statistics(self, data: pd.DataFrame) -> Dict[str, float]:
        """Calculate basic statistics for the dataset.

        Args:
            data: Input DataFrame to analyze.

        Returns:
            Dictionary containing calculated statistics.
        """
        stats={"mean":data.select_dtypes(include=["number"]).mean().mean(),"std":data.select_dtypes(include=["number"]).std().mean(),"count":len(data)}

        if self.verbose:
            print(f"Calculated statistics: {stats}")

        return stats


# Example of imports that should be organized by Ruff
from collections import defaultdict
import json
from datetime import datetime
import numpy as np


# Function demonstrating type hint gradual adoption
def process_variants(vcf_file: str, min_quality=20):
    """Process variant data from VCF file.

    This function demonstrates gradual typing - some parameters have hints,
    others don't (which is acceptable per team standards).

    Args:
        vcf_file: Path to VCF file.
        min_quality: Minimum quality score for filtering.

    Returns:
        Processed variant data.
    """
    # Simulate processing
    filtered_variants = []

    # This comment has trailing whitespace
    if not os.path.exists(vcf_file):
        raise FileNotFoundError(f"VCF file not found: {vcf_file}")

    # Intentionally poor formatting to test Ruff
    result={"file":vcf_file,"quality_threshold":min_quality,"variants":filtered_variants,"extra_data":[1,2,3,4,5]}

    return result


def demonstrate_docstring_styles():
    """Demonstrate proper Google-style docstring formatting.

    This function shows the expected docstring format for the GOSH team,
    including proper sections and formatting.

    Args:
        None

    Returns:
        str: A demonstration message.

    Raises:
        NotImplementedError: This is just a demo function.

    Example:
        >>> message = demonstrate_docstring_styles()
        >>> print(message)
        'Docstring formatting demonstration'
    """
    return "Docstring formatting demonstration"


# Example of code that should trigger linting warnings
def function_with_issues():

    unused_variable = "This should trigger a warning"
    print("Missing docstring should be flagged")
    # TODO: This should be caught by todo-tree extension


# Example of a long line that should be wrapped
very_long_variable_name_that_exceeds_line_length = "This string is intentionally very long to demonstrate line length formatting and should be wrapped or split across multiple lines according to our 120-character limit and this makes it even longer to really test the formatter"


# More bad formatting examples
def terrible_formatting(a,b,c,d,e,f):
    if a>0:x=a*2;y=b+c;return x+y+d+e+f
    else:return 0


weird_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
bad_dict={"key1":"value1","key2":"value2","key3":"value3","key4":"value4","key5":"value5"}


if __name__=="__main__":
    # Test the formatting tools
    analyzer=BioinformaticsAnalyzer("test_data.csv",verbose=True)

    # This should demonstrate format-on-save functionality
    print("Testing formatting tools...")
    print(f"Working directory: {os.getcwd()}")

    # Demonstrate various formatting scenarios
    result=poorly_formatted_function(1,2,[3,4,5]);print(f"Result: {result}")

    # More terrible formatting
    for i in range(5):print(i);print(i*2)

    test_data={"a":1,"b":2,"c":3};print(test_data)
