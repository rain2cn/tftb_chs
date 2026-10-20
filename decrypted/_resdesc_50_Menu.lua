local set = {}
set.name = "Menu"
set.setName = "Menu"
set.descriptionFilenameOverride = ""
set.logicalName = "<Menu>"
set.logicalDestination = "<>"
set.priority = 20
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Menu Game Data"
set.gameDataPriority = 0
set.gameDataEnableMode = "constant"
set.localDirIncludeBase = true
set.localDirRecurse = false
set.localDirIncludeOnly = nil
set.localDirExclude = 
{
    "_dev/"
}
set.gameDataArchives = 
{
    _currentDirectory .. "Borderlands_pc_chs_full_Menu.ttarch2",
    _currentDirectory .. "Borderlands_pc_Menu_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Menu_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Menu_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Menu_txmesh.ttarch2",
}
RegisterSetDescription(set)
