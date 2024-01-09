const getListStudentIds = (ids) => {
  if (!Array.isArray(ids)) {
    return [];
  }
  const studentIds = ids.map((item) => item.id);

  return studentIds;
};

export default getListStudentIds;
