#!/usr/bin/env python3
"""
Simple test to verify python-docx works
This tests the Word document library independently
"""

def test_docx():
    """Test if python-docx is installed and working"""
    print("=" * 60)
    print("Simple Word Document Test")
    print("=" * 60)
    print()

    # Test 1: Import docx
    print("1. Testing python-docx import...")
    try:
        from docx import Document
        from docx.shared import Pt, RGBColor
        from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
        print("   ✓ python-docx imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import python-docx: {e}")
        print()
        print("   FIX: Run this command:")
        print("   pip install python-docx")
        return False

    # Test 2: Create a document
    print("2. Creating a test Word document...")
    try:
        doc = Document()
        print("   ✓ Document object created")
    except Exception as e:
        print(f"   ✗ Failed to create document: {e}")
        return False

    # Test 3: Add content
    print("3. Adding content to document...")
    try:
        # Add a heading
        title = doc.add_heading('TextCopy Test Document', 0)
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        # Add a paragraph
        para = doc.add_paragraph()
        run = para.add_run("This is a test paragraph to verify Word document functionality.")
        run.font.name = "Calibri"
        run.font.size = Pt(11)

        # Add colored text
        para2 = doc.add_paragraph()
        colored_run = para2.add_run("This text should be blue.")
        colored_run.font.color.rgb = RGBColor(0, 102, 204)

        print("   ✓ Content added successfully")
    except Exception as e:
        print(f"   ✗ Failed to add content: {e}")
        return False

    # Test 4: Save document
    print("4. Saving document to test_output.docx...")
    try:
        import os

        # Create test output directory
        os.makedirs("test_output", exist_ok=True)

        output_file = "test_output/test_simple.docx"
        doc.save(output_file)
        print(f"   ✓ Document saved: {output_file}")
    except Exception as e:
        print(f"   ✗ Failed to save document: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test 5: Verify file exists
    print("5. Verifying file was created...")
    try:
        import os
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"   ✓ File exists: {output_file}")
            print(f"   ✓ File size: {file_size} bytes")
        else:
            print(f"   ✗ File does not exist: {output_file}")
            return False
    except Exception as e:
        print(f"   ✗ Error checking file: {e}")
        return False

    # Test 6: Test appending to existing document
    print("6. Testing append to existing document...")
    try:
        # Load the document we just created
        doc2 = Document(output_file)

        # Add more content
        doc2.add_paragraph("This is a second paragraph added after saving.")

        # Save again
        doc2.save(output_file)

        # Check file size increased
        new_size = os.path.getsize(output_file)
        print(f"   ✓ Appended to document successfully")
        print(f"   ✓ New file size: {new_size} bytes")

        if new_size > file_size:
            print(f"   ✓ File size increased as expected")
        else:
            print(f"   ⚠ Warning: File size did not increase")

    except Exception as e:
        print(f"   ✗ Failed to append to document: {e}")
        import traceback
        traceback.print_exc()
        return False

    print()
    print("=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
    print()
    print(f"Test document created at: {output_file}")
    print("You can open it to verify the content.")
    print()

    return True


if __name__ == '__main__':
    try:
        success = test_docx()
        if success:
            print("python-docx is working correctly!")
            print()
            print("Next step: Try running the full test with:")
            print("  python test_word.py")
        else:
            print("python-docx test failed.")
            print("Please fix the issues above before running TextCopy.")

        import sys
        sys.exit(0 if success else 1)

    except Exception as e:
        print(f"Test crashed with error: {e}")
        import traceback
        traceback.print_exc()
        import sys
        sys.exit(1)
