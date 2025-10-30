from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []
subjects = ["Math", "Science", "English"]  # Default subjects

@app.route('/')
def index():
    for s in students:
        if s['grades']:
            total = sum(s['grades'].values())
            avg = total / len(s['grades'])
            s['average'] = avg
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
            s['average'] = 0
            s['grade'] = '-'
    return render_template("index.html", students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        students.append({'name': name, 'roll': roll, 'grades': {}})
        return redirect(url_for('index'))
    return render_template("add_student.html")

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    global subjects
    if request.method == 'POST':
        new_subject = request.form['subject'].strip().capitalize()
        if new_subject and new_subject not in subjects:
            subjects.append(new_subject)
        return redirect(url_for('index'))
    return render_template("add_subject.html", subjects=subjects)

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

if __name__ == "__main__":
    app.run(debug=True)
