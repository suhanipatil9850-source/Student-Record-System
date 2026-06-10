from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', '').strip()
    filtered = students
    if query:
        filtered = [s for s in students if query.lower() in s['id'].lower() or query.lower() in s['name'].lower()]
    return render_template('index.html', students=filtered, query=query)

@app.route('/add', methods=['POST'])
def add_student():
    student_id = request.form.get('student_id', '').strip()
    name = request.form.get('name', '').strip()
    age = request.form.get('age', '').strip()
    grade = request.form.get('grade', '').strip()

    if student_id and name:
        students.append({
            'id': student_id,
            'name': name,
            'age': age,
            'grade': grade,
        })

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_student():
    original_id = request.form.get('original_id', '').strip()
    new_id = request.form.get('student_id', '').strip()
    new_name = request.form.get('name', '').strip()
    new_age = request.form.get('age', '').strip()
    new_grade = request.form.get('grade', '').strip()

    for student in students:
        if student['id'] == original_id:
            student['id'] = new_id or student['id']
            student['name'] = new_name or student['name']
            student['age'] = new_age or student['age']
            student['grade'] = new_grade or student['grade']
            break

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id', '').strip()
    global students
    students = [s for s in students if s['id'] != student_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
