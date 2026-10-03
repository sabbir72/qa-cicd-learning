import os
import xml.etree.ElementTree as ET

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def read_test_results(xml_file):
   

    results = []

    # XML file 
    if not os.path.exists(xml_file):
        return results

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for testcase in root.iter("testcase"):

        test_name = testcase.get(
            "name",
            "Unknown Test"
        )

        failure = testcase.find("failure")
        error = testcase.find("error")
        skipped = testcase.find("skipped")

        if failure is not None or error is not None:
            status = "FAIL"

        elif skipped is not None:
            status = "SKIP"

        else:
            status = "PASS"

        results.append([
            test_name,
            status
        ])

    return results


# ==========================================
# Read Smoke Results
# ==========================================

smoke_results = read_test_results(
    "reports/smoke/smoke-report.xml"
)


# ==========================================
# Read Regression Results
# ==========================================

regression_results = read_test_results(
    "reports/regression/regression-report.xml"
)


# ==========================================
# Combine Results
# ==========================================

all_results = []

for name, status in smoke_results:

    all_results.append([
        "Smoke",
        name,
        status
    ])


for name, status in regression_results:

    all_results.append([
        "Regression",
        name,
        status
    ])


# ==========================================
# Create PDF
# ==========================================

pdf_file = "qa-test-report.pdf"

document = SimpleDocTemplate(
    pdf_file,
    pagesize=A4
)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        "QA Automation Test Report",
        styles["Title"]
    )
)

content.append(
    Spacer(1, 20)
)


# ==========================================
# Table
# ==========================================

table_data = [
    [
        "Test Type",
        "Test Case",
        "Result"
    ]
]

# Test result 
if all_results:
    table_data.extend(all_results)
else:
    table_data.append([
        "-",
        "No test result found",
        "-"
    ])


table = Table(
    table_data,
    colWidths=[100, 320, 80]
)


# ==========================================
# Table Styling
# ==========================================

table.setStyle(
    TableStyle([

        # Header
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.grey
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.white
        ),

        # Border
        (
            "GRID",
            (0, 0),
            (-1, -1),
            1,
            colors.black
        ),

        # Padding
        (
            "PADDING",
            (0, 0),
            (-1, -1),
            6
        ),

        # Header alignment
        (
            "ALIGN",
            (0, 0),
            (-1, 0),
            "CENTER"
        ),

        # Result alignment
        (
            "ALIGN",
            (-1, 1),
            (-1, -1),
            "CENTER"
        ),

        # Vertical alignment
        (
            "VALIGN",
            (0, 0),
            (-1, -1),
            "MIDDLE"
        ),
    ])
)


content.append(table)

document.build(content)

print(f"PDF created: {pdf_file}")