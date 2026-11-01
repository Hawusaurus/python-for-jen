from payroll_bug import salary_after_raises, payslip_summary


def test_salary_after_raises():
    assert salary_after_raises(30000, 3, 2) == 31827.0
    assert salary_after_raises(30000, 3, 0) == 30000.0


def test_payslip_summary():
    assert payslip_summary("Jane Smith", 2500, 20) == (
        "Jane Smith: gross £2500.00, tax £500.00, net £2000.00"
    )


def test_payslip_summary_with_pence():
    assert payslip_summary("Omar Khan", 2345.5, 20) == (
        "Omar Khan: gross £2345.50, tax £469.10, net £1876.40"
    )
