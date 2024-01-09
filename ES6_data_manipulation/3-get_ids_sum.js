const getStudentIdsSum = (students) => {
  const idsSum = students
    .map((student) => student.id)
    .reduce((sum, studentCurrent) => sum + studentCurrent);

  return idsSum;
};

export default getStudentIdsSum;
