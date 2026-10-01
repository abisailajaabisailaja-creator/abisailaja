import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = None

if api_key:
    client = genai.Client(api_key=api_key)


def generate_local_document(
    document_type,
    name,
    company,
    date,
    role,
    address,
    terms
):

    if not name:
        name = "[Not Provided]"

    if not company:
        company = "[Not Provided]"

    if not date:
        date = "[Not Provided]"

    if not role:
        role = "[Not Provided]"

    if not address:
        address = "[Not Provided]"

    if not terms:
        terms = "[Not Provided]"


    if document_type == "Employment Contract":

        return f"""
EMPLOYMENT CONTRACT

1. PARTIES

This Employment Contract is entered into between:

Employee Name: {name}
Company / Organization: {company}

2. EMPLOYMENT POSITION

The employee will be appointed for the position of:
{role}

3. EFFECTIVE DATE

The employment will become effective from:
{date}

4. JOB RESPONSIBILITIES

The employee agrees to perform the duties and responsibilities
assigned by the employer in a professional manner.

5. WORKING HOURS

The employee shall follow the working hours and policies
specified by the employer.

6. SALARY AND COMPENSATION

Salary and other compensation shall be mutually agreed upon
between the employee and employer.

7. CONFIDENTIALITY

The employee shall maintain confidentiality of confidential
business, technical and organizational information.

8. INTELLECTUAL PROPERTY

Work created by the employee during employment shall be
handled according to the applicable company policies and law.

9. TERMINATION

Either party may terminate the employment subject to the
applicable agreement, notice requirements and law.

10. EMPLOYEE RESPONSIBILITIES

The employee shall follow company rules, policies and
professional standards.

11. EMPLOYER RESPONSIBILITIES

The employer shall provide the agreed employment conditions
and workplace responsibilities.

12. GOVERNING LAW

This agreement shall be governed by applicable laws.

13. ADDITIONAL TERMS

{terms}

14. SIGNATURES

Employee Signature: ______________________

Name: {name}

Date: ______________________


Employer Signature: ______________________

Company: {company}

Date: ______________________


DISCLAIMER

This document is an AI-assisted draft for informational purposes
only. It should be reviewed by a qualified legal professional
before use.
"""


    elif document_type == "NDA":

        return f"""
NON-DISCLOSURE AGREEMENT

1. PARTIES

Disclosing / Receiving Party:
{name}

Company / Organization:
{company}

2. PURPOSE

The parties intend to protect confidential information shared
for business or professional purposes.

3. CONFIDENTIAL INFORMATION

Confidential information may include business information,
technical information, financial information, documents,
processes and other non-public information.

4. OBLIGATIONS

The receiving party shall not disclose confidential information
to unauthorized persons.

5. EXCEPTIONS

Information that is publicly available or lawfully obtained from
another source may not be considered confidential.

6. DURATION

Confidentiality obligations shall continue according to the
agreed terms and applicable law.

7. INTELLECTUAL PROPERTY

All intellectual property shall remain with its respective owner
unless otherwise agreed in writing.

8. GOVERNING LAW

This agreement shall be governed by applicable laws.

9. ADDITIONAL TERMS

{terms}

10. SIGNATURES

Party Signature: ______________________

Name: {name}

Date: ______________________


Company Signature: ______________________

Company: {company}

Date: ______________________


DISCLAIMER

This document is an AI-assisted draft for informational purposes
only. It should be reviewed by a qualified legal professional
before use.
"""


    elif document_type == "Lease Agreement":

        return f"""
LEASE AGREEMENT

1. LANDLORD

Landlord / Owner:
{name}

2. TENANT

Tenant / Organization:
{company}

3. PROPERTY

Property Address:
{address}

4. LEASE TERM

Effective Date:
{date}

5. PURPOSE

The property shall be used for the purpose agreed upon by the
landlord and tenant.

6. RENT

The rent amount and payment schedule shall be mutually agreed
upon by the parties.

7. SECURITY DEPOSIT

Any security deposit shall be handled according to the agreed
terms and applicable law.

8. MAINTENANCE

The parties shall be responsible for maintenance according to
their agreed responsibilities.

9. TERMINATION

The agreement may be terminated according to the agreed terms
and applicable law.

10. ADDITIONAL TERMS

{terms}

11. SIGNATURES

Landlord Signature: ______________________

Name: {name}

Date: ______________________


Tenant Signature: ______________________

Name: {company}

Date: ______________________


DISCLAIMER

This document is an AI-assisted draft for informational purposes
only. It should be reviewed by a qualified legal professional
before use.
"""


    elif document_type == "Internship Agreement":

        return f"""
INTERNSHIP AGREEMENT

1. INTERN DETAILS

Intern Name:
{name}

2. ORGANIZATION

Organization:
{company}

3. INTERNSHIP POSITION

Position / Purpose:
{role}

4. INTERNSHIP DURATION

Start Date:
{date}

5. RESPONSIBILITIES

The intern shall perform assigned tasks and responsibilities
under appropriate supervision.

6. WORKING HOURS

The intern shall follow the working hours and policies
specified by the organization.

7. TRAINING

The organization may provide training and practical learning
opportunities related to the internship.

8. CONFIDENTIALITY

The intern shall maintain confidentiality of organizational
information.

9. INTELLECTUAL PROPERTY

Work created during the internship shall be handled according
to organizational policies and applicable law.

10. TERMINATION

The internship may be terminated according to the agreed terms.

11. ADDITIONAL TERMS

{terms}

12. SIGNATURES

Intern Signature: ______________________

Name: {name}

Date: ______________________


Organization Signature: ______________________

Organization: {company}

Date: ______________________


DISCLAIMER

This document is an AI-assisted draft for informational purposes
only. It should be reviewed by a qualified legal professional
before use.
"""


    else:

        return f"""
LEGAL DOCUMENT

Document Type:
{document_type}

Name:
{name}

Company / Organization:
{company}

Effective Date:
{date}

Purpose / Role:
{role}

Address:
{address}

Additional Terms:
{terms}


SIGNATURE

Signature: ______________________

Date: ______________________


DISCLAIMER

This document is an AI-assisted draft for informational purposes
only. It should be reviewed by a qualified legal professional
before use.
"""


def generate_legal_document(
    document_type,
    name,
    company,
    date,
    role,
    address,
    terms
):

    prompt = f"""
Create a professional {document_type}.

Name: {name}
Company: {company}
Effective Date: {date}
Role / Purpose: {role}
Address: {address}
Additional Terms: {terms}

Use clear headings, numbered clauses and a signature section.
Do not invent missing information.
"""


    # Try Gemini first
    if client:

        try:

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as e:

            error_text = str(e)

            print(
                "Gemini unavailable. "
                "Using local document template."
            )

            print(error_text)


    # Fallback
    return generate_local_document(
        document_type,
        name,
        company,
        date,
        role,
        address,
        terms
    )