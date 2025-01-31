import csv
import os
from pypdf import PdfReader, PdfWriter

class Form:
    def __init__(self, tenant_1:str, tenant_2:str, rent:int, unit_num:str):
        self.tenant_1 = tenant_1
        self.tenant_2 = tenant_2
        self.rent = rent
        self.unit_num = unit_num

    def all(self):
        self.master()
        self.smoke()
        self.bedbug()
        self.flood()
        self.inspection()
        self.mold()
        self.plumbing()
        self.pest()

    def master(self):
        template_pdf = 'templates/LLC_Master_Rental_Agreement_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/LLC_Master_Rental_Agreement.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        writer.update_page_form_field_values(
            writer.pages[0], 
            {"TenantsLessee":self.tenant_1,
            "TenantsLessee_2":self.tenant_2,
            "Unit Number": self.unit_num,
            "Monthly Rental Rate":f"{self.rent:.2f}",
            "t": f"{self.rent:.2f}",
            "Late Charge": f"{round(self.rent*.06,2):.2f}",
            "First months rent of": f"{self.rent:.2f}",
            "total payment of 101":f"{self.rent*2:.2f}",
            "equaling amount": f"{round(self.rent*.06,2):.2f}",
            "payment of": f"{self.rent:.2f}"
            },
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def inspection(self):
        template_pdf = 'templates/131_Move_in_Move_Out_Inspection_Checklist_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/131_Move_in_Move_Out_Inspection_Checklist.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Resident Names": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Resident Names": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"Rental Unit Address": f"4435 Arizona Street, #{self.unit_num}"},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    def flood(self):
        template_pdf = 'templates/158_-_Flood_Disclosure_Addendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/158_-_Flood_Disclosure_Addendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"between 2": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"between 2": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"unit number": self.unit_num},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def bedbug(self):
        template_pdf = 'templates/148_Bedbug_Addendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/148_Bedbug_Addendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Text3": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Text3": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )
        writer.update_page_form_field_values(
            writer.pages[0],
            {"Text5": self.unit_num},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def pest(self):
        template_pdf = 'templates/148B_-PEST_CONTROL_ADDENDUM_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/148B_-PEST_CONTROL_ADDENDUM.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"hereby known as OwnerAgent and": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"hereby known as OwnerAgent and": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"unit number": self.unit_num},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def mold(self):
        template_pdf = 'templates/149_Mold Addendum To Lease_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/149_Mold Addendum To Lease.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"TENANTS for the premises located at": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"TENANTS for the premises located at": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"CA": f"4435 Arizona Street, #{self.unit_num}, San Diego"},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def plumbing(self):
        template_pdf = 'templates/PlumbingAddendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/PlumbingAddendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        writer.update_page_form_field_values(
            writer.pages[0], 
            {"TENANT":self.tenant_1,
            "TENANT and":self.tenant_2,
            "in the city of": self.unit_num
            },
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    def smoke(self):
        template_pdf = 'templates/SmokeFreeAddendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/SmokeFreeAddendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"THIS AGREEMENT made and entered into between": self.tenant_1},
                auto_regenerate=False
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"THIS AGREEMENT made and entered into between": f"{self.tenant_1}, {self.tenant_2}"},
                auto_regenerate=False
            )
        writer.update_page_form_field_values(
            writer.pages[0],
            {"undefined": self.unit_num},
            auto_regenerate=False
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)