from flask import Flask, jsonify, request

app = Flask(__name__)

staff_members = []

@app.route('/staff', methods=['GET'])
def get_staff():
    return jsonify(staff_members)

@app.route('/staff', methods=['POST'])
def add_staff():
    staff = request.get_json()
    staff['id'] = len(staff_members) + 1
    staff_members.append(staff)
    return jsonify(staff), 201

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    staff = next((s for s in staff_members if s['id'] == id), None)
    if not staff:
        return jsonify({'message': 'Staff not found'}), 404
    data = request.get_json()
    staff.update(data)
    return jsonify(staff)

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    staff = next((s for s in staff_members if s['id'] == id), None)
    if not staff:
        return jsonify({'message': 'Staff not found'}), 404
    staff_members.remove(staff)
    return jsonify({'message': 'Staff deleted'})

if __name__ == '__main__':
    app.run(debug=True)
