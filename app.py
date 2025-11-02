from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------------
# Global Data Storage
# -------------------------
students = []
subjects = ["Math", "Science", "English"]  # Default subjects

# -------------------------
# Home Page
# -------------------------
@app.route('/')
def index():
    for s in students:
        grades = s['grades']
        if grades:
            total = sum(grades.values())
            max_total = len(subjects) * 100
            avg = total / len(subjects)

            s['total'] = total
            s['max_total'] = max_total
            s['average'] = round(avg, 2)

            # Grade calculation
            if avg >= 90:
                s['grade'] = 'A'
            elif avg >= 75:
                s['grade'] = 'B'
            elif avg >= 60:
                s['grade'] = 'C'
            elif avg >= 40:
                s['grade'] = 'D'
            else:
                s['grade'] = 'F'
        else:
            s['total'] = 0
            s['max_total'] = len(subjects) * 100
            s['average'] = 0
            s['grade'] = '-'

    return render_template("index.html", students=students)

# -------------------------
# Add Student
# -------------------------
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']

        # Check for duplicate roll number
        for s in students:
            if s['roll'] == roll:
                return redirect(url_for('index'))

        students.append({
            'name': name,
            'roll': roll,
            'grades': {}
        })
        return redirect(url_for('index'))
    return render_template("add_student.html")

# -------------------------
# Add Subject
# -------------------------
@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    global subjects
    if request.method == 'POST':
        new_subject = request.form['subject'].strip().capitalize()
        if new_subject and new_subject not in subjects:
            subjects.append(new_subject)
        return redirect(url_for('index'))
    return render_template("add_subject.html", subjects=subjects)

# -------------------------
# Add Marks for a Student
# -------------------------
@app.route('/add_marks/<roll>', methods=['GET', 'POST'])
def add_marks(roll):
    student = None
    for st in students:
        if st['roll'] == roll:
            student = st
            break
    if not student:
        return redirect(url_for('index'))

    if request.method == 'POST':
        for sub in subjects:
            mark = request.form.get(sub)
            if mark:
                try:
                    student['grades'][sub] = float(mark)
                except ValueError:
                    student['grades'][sub] = 0.0
        return redirect(url_for('index'))

    return render_template("add_marks.html", student=student, subjects=subjects)

# -------------------------
# Run Flask App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
